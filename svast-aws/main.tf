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
    key    = "terraform/static-frontend-website.tfstate"
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

# Server App:
module "booking-cal-app" {
  source    = "../lambda-server"
  app_name  = "booking-cal"
  image_tag = "0.0.4"
}
output "booking-cal-app-url" {
  value = module.booking-cal-app.base_url
}