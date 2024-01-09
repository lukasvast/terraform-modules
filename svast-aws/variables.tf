variable "r53_zone" {
  type = map(string)

  default = {
    domain_name                           = "svast.eu"
    cloudfront_domain_ssl_certificate_arn = "arn:aws:acm:us-east-1:199000118951:certificate/9832bc2d-56e0-4f0a-ba1a-9cdc2bfa297e"
  }
}

variable "elevate_agency_r53_zone" {
  type = map(string)

  default = {
    domain_name                           = "elevate-agency.net"
    cloudfront_domain_ssl_certificate_arn = "arn:aws:acm:us-east-1:199000118951:certificate/b00aa3e9-f27f-4a36-8f1c-dfd394e4b41e"
  }
}

variable "websites" {
  type = map(object({
    website_name       = string
    enable_apex_domain = bool
  }))
  default = {
    website-1 = {
      website_name       = "manuela-luka"
      enable_apex_domain = false
    }
  }
}

variable "elevate_agency_websites" {
  type = map(object({
    website_name       = string
    enable_apex_domain = bool
  }))
  default = {
    website-1 = {
      website_name       = "elevate-agency"
      enable_apex_domain = true
    }
  }
}