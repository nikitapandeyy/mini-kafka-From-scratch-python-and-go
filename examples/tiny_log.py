class TinyLog:
    def __init__(self):
        self.messages = []          # the log

    def append(self, msg):
        self.messages.append(msg)
        return len(self.messages) - 1   # the offset

    def read(self, offset):
        return self.messages[offset:]   # reading doesn't delete


log = TinyLog()
log.append("order 1")
log.append("order 2")
log.append("order 3")

# Two independent consumers with their own offsets
email_offset = 0
analytics_offset = 2

print("email reads:", log.read(email_offset))
print("analytics reads:", log.read(analytics_offset))