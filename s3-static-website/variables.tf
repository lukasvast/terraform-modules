variable "prefix" {
  type = string
}

variable "bucket_prefix" {
  type = string
}

variable "websites" {
  type = map(any)
}

variable "r53_zone" {
  type = map(any)
}

variable "encryption" {
  type    = bool
  default = true
}