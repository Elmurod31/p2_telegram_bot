from aiogram.fsm.state import StatesGroup, State

#register
class UserRegisterState(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    address= State()


#ichimliklar
class UserIchimliklarState(StatesGroup):
    nomi = State()
    hajmi = State()
    soni = State()
    shakarli = State()


#Mevalar
class UserMevalarState(StatesGroup):
    nomi = State()
    ogirligi = State()
    rangi = State()
    shakli = State()


#go'sht mahsulotlari
class UserGoshtState(StatesGroup):
    turi = State()
    ogirligi = State()
    narxi = State()
    shakli = State()

#sut mahsulotlari
class UserSutState(StatesGroup):
    nomi = State()
    yog_mikdori = State()
    ogirligi = State()
    narxi = State()

# Soatlar
class UserSoatState(StatesGroup):
    brendi = State()
    materiali = State()
    narxi = State()
    turi = State()

# Oyoq kiyimlar
class UserOyoqKiyimState(StatesGroup):
    brendi = State()
    razmeri = State()
    materyali = State()
    narxi = State()

# Elektromobillar
class UserElektromobilState(StatesGroup):
    modeli = State()
    quvvat = State()
    batareya = State()
    narxi = State()

# Smartfonlar
class UserSmartfonState(StatesGroup):
    brendi = State()
    modeli = State()
    xotira = State()
    narxi = State()

# Notebooklar
class UserNotebookState(StatesGroup):
    brendi = State()
    protsessor = State()
    ram = State()
    narxi = State()

# Kompyuterlar
class UserKompyuterState(StatesGroup):
    brendi = State()
    protsessor = State()
    videokarta = State()
    narxi = State()
