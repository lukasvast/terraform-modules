variable "r53_zone" {
  type = map(string)

  default = {
    domain_name                           = "julija-crikvenica.com"
    cloudfront_domain_ssl_certificate_arn = "arn:aws:acm:us-east-1:199000118951:certificate/1e6550ae-3c2c-43e9-b5b3-75749406e7ab"
  }
}

variable "websites" {
  type = map(object({
    website_name       = string
    enable_apex_domain = bool
  }))
  default = {
    website-1 = {
      website_name       = "www"
      enable_apex_domain = true
    }
  }
}