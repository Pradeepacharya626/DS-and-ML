import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b) :
    result = a+b
    logger.debug(f"Addition {a}+{b}={result}")
    return result

def sub(a,b) :
    result = a-b
    logger.debug(f"subtraction {a}-{b}={result}")
    return result

def mul(a,b) :
    result = a*b
    logger.debug(f"multiplication {a}*{b}={result}")
    return result

def div(a,b) :
    try :
        result = a/b
        logger.debug(f"Addition {a}/{b}={result}")
        return result
    except ZeroDivisionError :
        logger.error("Zero devision error")
        return None

add(15,10)
sub(10,5)
mul(3,6)
div(5,0)