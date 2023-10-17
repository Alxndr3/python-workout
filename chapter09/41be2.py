"""Create a Phone class that represents a mobile phone. (Are there still
nonmobile phones?) The phone should implement a dial method that dials a
phone number (or simulates doing so). Implement a SmartPhone subclass
that uses the Phone.dial method but implements its own run_app method.
Now implement an iPhone subclass that implements not only a run_app
method, but also its own dial method, which invokes the parent’s dial
method but whose output is all in lowercase as a sign of its coolness."""


class Phone:

    def __init__(self):
        pass

    def dial(self):
        print('Dilling')


class SmartPhone(Phone):

    def run_app(self):
        print('Running App')


"""Solution to chapter 9, exercise 41, beyond 2: phone"""


class PhoneBS:
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'


class SmartPhoneBS(Phone):
    def run_app(self, app_name):
        return f'Running an app: {app_name}'


class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()


smart_phone1 = SmartPhone()
smart_phone1.run_app()
smart_phone1.dial()

