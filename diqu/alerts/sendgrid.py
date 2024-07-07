import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from diqu.utils.log import logger
from diqu.utils.meta import ResultCode

NO_REPLY = "diqu-email@noreply.com"


def alert(data) -> ResultCode:
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    SENDGRID_MAILING_LIST = os.environ.get("SENDGRID_MAILING_LIST")
    SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID")
    SENDGRID_FROM = os.environ.get("SENDGRID_FROM") or NO_REPLY
    if not SENDGRID_API_KEY or not SENDGRID_MAILING_LIST:
        logger.error("❌ SENDGRID_API_KEY or SENDGRID_MAILING_LIST are not set")
        return ResultCode.FAILED
        
    msg = Mail(
        from_email=SENDGRID_FROM,
        to_emails=SENDGRID_MAILING_LIST.split(","),
        is_multiple=True,
        dynamic_template_data={
            "date": data["CHECK_TIMESTAMP"].iloc[0],
            "fail_count": data[data["TEST_STATUS"] == "fail"].shape[0],
            "warn_count": data[data["TEST_STATUS"] == "warn"].shape[0],
            "pass_count": data[data["TEST_STATUS"] == "pass"].shape[0],
            "deperecated_count": data[data["TEST_STATUS"] == "deprecate"].shape[0],
        },
        template_id=SENDGRID_TEMPLATE_ID,
    )

    try:
        client = SendGridAPIClient(SENDGRID_API_KEY)
        client.send(msg)

        logger.info("✅ Done > Sendgrid")
        return ResultCode.SUCCEEDED
    except Exception as e:
        logger.error(f"❌ Sendgrid error: {e}")
        return ResultCode.FAILED
