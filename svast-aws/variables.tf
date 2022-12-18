variable "r53_zone" {
  type = map(string)

  default = {
    domain_name                           = "svast.eu"
    cloudfront_domain_ssl_certificate_arn = "arn:aws:acm:us-east-1:199000118951:certificate/9832bc2d-56e0-4f0a-ba1a-9cdc2bfa297e"
  }
}

variable "websites" {
  type = map(object({
    website_name = string
  }))
  default = {
    website-1 = {
      website_name = "manuela-luka"
    }
  }
}