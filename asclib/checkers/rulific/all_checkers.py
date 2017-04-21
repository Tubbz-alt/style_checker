from asclib.checkers.rulific.copyright import CopyrightRuleChecker
from asclib.checkers.rulific.rcs_keywords import RCSKeywordsRuleChecker
from asclib.checkers.rulific.dos_eol import DosEolRuleChecker
from asclib.checkers.rulific.eol_consistency import EolConsistencyRuleChecker
from asclib.checkers.rulific.first_line_comment \
    import FirstLineCommentRuleChecker
from asclib.checkers.rulific.last_line_eol import LastLineEOLRuleChecker
from asclib.checkers.rulific.line_length import LineLengthRuleChecker
from asclib.checkers.rulific.trailing_spaces import TrailingSpaceRuleChecker

ALL_RULIFIC_CHECKERS = (
    LineLengthRuleChecker,
    DosEolRuleChecker,
    EolConsistencyRuleChecker,
    TrailingSpaceRuleChecker,
    LastLineEOLRuleChecker,
    FirstLineCommentRuleChecker,
    RCSKeywordsRuleChecker,
    CopyrightRuleChecker,
    )