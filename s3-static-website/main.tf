/*
S3 BUCKET FOR FRONTEND
*/
resource "aws_s3_bucket" "frontend_bucket" {
  for_each = var.websites

  bucket = "${var.bucket_prefix}-${each.value["website_name"]}-frontend"

  tags = {
    Name = "${var.bucket_prefix}-${each.value["website_name"]}-frontend"
  }
}

resource "aws_s3_bucket_public_access_block" "frontend_bucket_public_access_block" {
  for_each = var.websites

  bucket = aws_s3_bucket.frontend_bucket[each.key].id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "frontend_bucket_encryption" {
  for_each = var.websites

  bucket = aws_s3_bucket.frontend_bucket[each.key].bucket

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_policy" "frontend_bucket_policy" {
  for_each = var.websites

  bucket = aws_s3_bucket.frontend_bucket[each.key].id

  policy = <<END
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::${var.bucket_prefix}-${each.value["website_name"]}-frontend/*"
            ],
            "Effect": "Allow",
            "Principal": {
                "AWS": "${aws_cloudfront_origin_access_identity.frontend_bucket_origin_access_identity[each.key].iam_arn}"
            }
        }
    ]
}
END
}

resource "aws_cloudfront_origin_access_identity" "frontend_bucket_origin_access_identity" {
  for_each = var.websites

  comment = "${var.bucket_prefix}-${each.value["website_name"]}-frontend"
}

/*
CLOUDFRONT DISTRIBUTION
*/
resource "aws_cloudfront_distribution" "frontend_bucket_distribution" {
  for_each = var.websites

  origin {
    domain_name = aws_s3_bucket.frontend_bucket[each.key].bucket_domain_name
    origin_id   = "s3-cloudfront"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.frontend_bucket_origin_access_identity[each.key].cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  comment             = "${var.prefix}-${each.value["website_name"]}.${var.r53_zone.domain_name}"
  price_class         = "PriceClass_100"
  aliases             = ["${var.prefix}-${each.value["website_name"]}.${var.r53_zone.domain_name}"]
  wait_for_deployment = true

  default_cache_behavior {
    allowed_methods = [
      "GET",
      "HEAD",
      "OPTIONS"
    ]

    cached_methods = [
      "GET",
      "HEAD",
      "OPTIONS"
    ]

    target_origin_id = "s3-cloudfront"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    compress               = true
    min_ttl                = 60
    default_ttl            = 3600
    max_ttl                = 86400
  }


  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = var.r53_zone.cloudfront_domain_ssl_certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2018"
  }

  custom_error_response {
    error_code            = 404
    response_code         = 200
    error_caching_min_ttl = 300
    response_page_path    = "/index.html"
  }

  custom_error_response {
    error_code            = 403
    response_code         = 200
    error_caching_min_ttl = 300
    response_page_path    = "/index.html"
  }

  tags = {
    Website = each.value["website_name"]
  }
}

/*
DNS ENTRY
*/
data "aws_route53_zone" "frontend_bucket_selected_dns_zone" {
  name = "${var.r53_zone.domain_name}."
}

resource "aws_route53_record" "frontend_bucket_route53_record" {
  for_each = var.websites

  zone_id = data.aws_route53_zone.frontend_bucket_selected_dns_zone.zone_id
  name    = "${var.prefix}-${each.value["website_name"]}.${var.r53_zone.domain_name}"
  type    = "A"

  alias {
    name    = aws_cloudfront_distribution.frontend_bucket_distribution[each.key].domain_name
    zone_id = "Z2FDTNDATAQYW2"

    //HardCoded value for CloudFront
    evaluate_target_health = false
  }
}