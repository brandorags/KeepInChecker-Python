from pony.orm import *


db = Database('sqlite', 'KeepInChecker.sqlite', create_db=False)


class Packets(db.Entity):
    PacketId = PrimaryKey(int, auto=True)
    DateReceived = Required(str)
    Timezone = Required(str)
    Get = Optional(str)
    Host = Optional(str)
    Referer = Optional(str)

    def get_PacketId(self):
        if not self.PacketId:
            return ''

        return self.PacketId

    def get_DateReceived(self):
        if not self.DateReceived:
            return ''

        return self.DateReceived

    def get_Timezone(self):
        if not self.Timezone:
            return ''

        return self.Timezone

    def get_Get(self):
        if not self.Get:
            return ''

        return self.Get

    def get_Host(self):
        if not self.Host:
            return ''

        return self.Host

    def get_Referer(self):
        if not self.Referer:
            return ''

        return self.Referer


db.generate_mapping(check_tables=True, create_tables=False)
