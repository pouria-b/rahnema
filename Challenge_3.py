class FeatureFlagSystem2:
    # Constructor
    def __init__(self, n_features_max, n_users_max):
        self.n_features_max = n_features_max
        self.n_users_max = n_users_max
        # Initializations
        self.features_set = set()
        self.user_features_list = [ set() for _ in range(self.n_users_max) ]
        self.features_enable_all = set()
        return
    # قابلیت مشخص‌شده را به سیستم اضافه میکند. این قابلیت در ابتدا برای همه‌ی کاربران غیرفعال است..
    def addFeature(self, feature: str):
        self.features_set.add(feature)
        return
    #  قابلیت مشخص‌شده را به طور کامل از سیستم حذف می‌کند.
    def disableFeature(self, feature: str):
        self.features_set.remove(feature)
        self.features_enable_all.remove(feature)
        return
    #  این متد یک قابلیت را برای تمام کاربران فعال می‌کند.
    def enableFeature(self, feature: str):
        self.features_enable_all.add(feature)
        return
    #  این متد یک قابلیت را برای گروهی مشخص از کاربران فعال می‌کند.
    def enableFeatureForUsers(
            self,
            feature: str,    # نام قابلیت
            userIds: list,  # آیدی کاربرانی که این قابلیت برایشان فعال می‌شود
        ):
        for userId in userIds:
            user_list = self.user_features_list[userId]
            user_list.add(feature)
        return
    # این متد بررسی می‌کند که آیا قابلیت داده‌شده برای کاربر مشخص فعال است یا نه.
    # اگر این قابلیت به صورت کلی یا برای آن کاربر فعال شده باشد، خروجی true خواهد بود.
    def isFeatureEnabled(self, feature: str, userId: int) -> bool:
        user_list = self.user_features_list[userId]
        return (feature in self.features_enable_all ) or (feature in user_list)
    # لیستی از تمام قابلیت‌هایی که برای کاربر داده‌شده فعال هستند را برمی‌گرداند.
    def listEnabledFeatures(self, userId: int) -> list:
        user_list = list(
            self.user_features_list[userId]
        ) + list(
            self.features_enable_all
        )
        return user_list
    



flags = FeatureFlagSystem2(n_features_max=1000, n_users_max=10_000)

print( flags.addFeature("dark-mode") )  # قابلیت دارک مود به سیستم اضافه میشود
print( flags.addFeature("new-ui") )  # قابلیت UI جدید به سیستم اضافه میشود
print( flags.enableFeature("dark-mode") )  # تمام کاربران میتوانند از قابلیت دارک مود استفاده نمایند
print( flags.enableFeatureForUsers("new-ui", [42, 77]) )  # // تنها کاربران با آیدی 42 و 77 می‌توانند از UI جدید استفاده کنند
print( flags.isFeatureEnabled("dark-mode", 123) )  # true
print( flags.isFeatureEnabled("new-ui", 42) )  # true
print( flags.isFeatureEnabled("new-ui", 12) )  # false
print( flags.isFeatureEnabled("promo", 99) )  # false
print( flags.listEnabledFeatures(42) )  # ["new-ui", "dark-mode"]
print( flags.listEnabledFeatures(2) )  # ["dark-mode"]