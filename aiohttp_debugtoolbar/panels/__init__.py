from .headers import HeaderDebugPanel
from .performance import PerformanceDebugPanel
from .request_vars import RequestVarsDebugPanel
from .routes import RoutesDebugPanel
from .settings import SettingsDebugPanel
from .traceback import TracebackPanel
from .middlewares import MiddlewaresDebugPanel
from .versions import VersionDebugPanel

# flake8
(HeaderDebugPanel, PerformanceDebugPanel, SettingsDebugPanel, TracebackPanel,
 MiddlewaresDebugPanel, VersionDebugPanel, RoutesDebugPanel,
 RequestVarsDebugPanel)
