import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("warning, no code here", SyntaxWarning)
warnings.warn("warning, module not import", ImportWarning)