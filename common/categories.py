from enum import Enum


class Categories(int, Enum):
    BLOGS = 0
    NEWS = 1
    ECONOMICS = 2
    FINANCES = 3
    POLITICS = 4
    LAW = 5
    MARKETING = 6
    CRYPTOCURRENCIES = 7
    BUSINESS = 8
    SHOWBIZ = 9
    ENTERTAINMENT = 10
    ART = 11
    FILMS = 12
    PICTURES = 13
    GAMES = 14
    SPORT = 15
    TRAVELLING = 16
    MUSIC = 17
    FASHION = 18
    CULINARY = 19
    PHRASES = 20
    DIY = 21
    TECHNOLOGIES = 22
    APPLICATIONS = 23
    EDUCATION = 24
    MEDICINE = 25
    PSYCHOLOGY = 26
    DESIGN = 27
    OTHER = 28


names = {
    Categories.BLOGS: "Блоги",
    Categories.NEWS: "Новости и СМИ",
    Categories.ECONOMICS: "Экономика",
    Categories.FINANCES: "Финансы",
    Categories.POLITICS: "Политика",
    Categories.LAW: "Право",
    Categories.MARKETING: "Маркетинг, PR, реклама",
    Categories.CRYPTOCURRENCIES: "Криптовалюты",
    Categories.BUSINESS: "Бизнес и стартапы",
    Categories.SHOWBIZ: "Шоубиз",
    Categories.ENTERTAINMENT: "Развлечения и юмор",
    Categories.ART: "Искусство",
    Categories.FILMS: "Видео и фильмы",
    Categories.PICTURES: "Картинки и фото",
    Categories.GAMES: "Игры",
    Categories.SPORT: "Спорт",
    Categories.TRAVELLING: "Путешествия",
    Categories.MUSIC: "Музыка",
    Categories.FASHION: "Мода и красота",
    Categories.CULINARY: "Еда и кулинария",
    Categories.PHRASES: "Цитаты",
    Categories.DIY: "Рукоделие",
    Categories.TECHNOLOGIES: "Технологии",
    Categories.APPLICATIONS: "Софт и приложения",
    Categories.EDUCATION: "Образование и познавательное",
    Categories.MEDICINE: "Здоровье и медицина",
    Categories.PSYCHOLOGY: "Психология",
    Categories.DESIGN: "Дизайн",
    Categories.OTHER: "Другое",
}
