def logSender():
    import logging
    from logging.handlers import SysLogHandler
    import sockets
    class ContextFilter(logging.Filter):
        hostname = sockets.gethostname()
        def filter(self, record):
            record.hostname = ContextFilter.hostname
            return True
    syslog = SysLogHandler(address=('logsN.papertrailapp.com', XXXXX))
    syslog.addFilter(ContextFilter())
    format = '%(asctime)s %(hostname)s YOUR_APP: %(message)s'
    formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
    syslog.setFormatter(formatter)
    logging = logging.getLogger()
    logging.addHandler(syslog)
    logging.setLevel(logging.INFO)
    tb = ""
    try:
        a = 1/0
    except:
        tb = traceback.format_exc()
        lines = tb.split('\n')
        for l in lines:
            logger.info(l)