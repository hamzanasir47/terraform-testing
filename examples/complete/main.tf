module "ssm_basic" {
  # Set source and version from TFC registry
  # https://app.terraform.io/app/lplfinancial-platforms/registry/modules/private/lplfinancial-platforms/service-ssm-parameter
  source = "../../"

  name  = "basic-example"
  type  = "String"
  value = "example-parameter-value"
}
