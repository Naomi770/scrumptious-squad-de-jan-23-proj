resource "aws_cloudwatch_event_rule" "extract_scheduler" {
    name_prefix = "extract-scheduler-"
    schedule_expression = "rate(1 minute)"
}

resource "aws_cloudwatch_event_target" "extract_lambda_target" {
    rule = aws_cloudwatch_event_rule.extract_scheduler.name
    arn  = aws_lambda_function.extract_lambda.arn
}

resource "aws_lambda_permission" "allow_extract_scheduler" {
    action = "lambda:InvokeFunction"
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.extract_scheduler.arn
    function_name = aws_lambda_function.extract_lambda.function_name
    source_account = data.aws_caller_identity.current.account_id
}
