from pathlib import Path
import re
 
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid
def isEmpty(string: str):
    return len(string) == 0

# Caminhos
ROOT = Path(__file__).parent
LOGO_PATH = ROOT / "files" / "logo-pepsi.png"

#colors
PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'
# Sizing

BIG_FONT_SIZE = 30
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 10
MINIMUN_WIDTH = 500