terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.2.0"
    }
  }

  required_version = ">=1.0.0"
}

terraform {
  backend "s3" {
    bucket = "svast-aws-tf-state"
    key    = "terraform/app-julija/static-frontend-website.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}

# Prerequsite:
# - r53 domain
# - self renewing ssl certificate in us-east-1 region
module "static-frontend-website" {
  source        = "git::https://github.com/lukasvast/terraform-modules.git//s3-static-website?ref=main"
  bucket_prefix = "web"
  websites      = var.websites
  r53_zone      = var.r53_zone
}

# Zone APEX Alias
data "aws_route53_zone" "frontend_bucket_selected_dns_zone" {
  name = "${var.r53_zone.domain_name}."
}
resource "aws_route53_record" "www" {
  zone_id = data.aws_route53_zone.frontend_bucket_selected_dns_zone.zone_id
  name    = var.r53_zone.domain_name
  type    = "A"

  alias {
    name                   = "www.${var.r53_zone.domain_name}"
    zone_id                = data.aws_route53_zone.frontend_bucket_selected_dns_zone.zone_id
    evaluate_target_health = true
  }
}