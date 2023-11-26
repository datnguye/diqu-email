from diqu.utils.log import logger
from diqu.utils.meta import ResultCode


def alert(data) -> ResultCode:
    logger.info("✅ Done > Sendgrid")