from pony.orm import *


db = Database('sqlite', 'KeepInChecker.sqlite', create_db=False)


class Users(db.Entity):
    UserId = PrimaryKey(int, auto=True)
    UserName = Required(str)
    UserEmail = Required(str)
    UserEmailPassword = Required(str)
    PartnerEmail = Required(str)
    EmailFrequency = Required(str)

    def get_UserId(self):
        if not self.UserId:
            return ''

        return self.UserId

    def get_UserName(self):
        if not self.UserName:
            return ''

        return self.UserName

    def get_UserEmail(self):
        if not self.UserEmail:
            return ''

        return self.UserEmail

    def get_UserEmailPassword(self):
        if not self.UserEmailPassword:
            return ''

        return self.UserEmailPassword

    def get_PartnerEmail(self):
        if not self.PartnerEmail:
            return ''

        return self.PartnerEmail

    def get_EmailFrequency(self):
        if not self.EmailFrequency:
            return ''

        return self.EmailFrequency


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
