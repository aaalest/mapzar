from models.category import Category

ROOT_CATEGORY: Category = Category("root", "Головне меню", [
    Category("food", "🥩 Продукти харчування", [
        Category("vegetables_fruits", "Овочі, фрукти та зелень", [
            Category("vegetables", "Овочі"),
            Category("fruits", "Фрукти"),
            Category("berries", "Ягоди"),
            Category("greens_herbs", "Зелень та трави"),
            Category("mushrooms", "Гриби"),
        ]),
        Category("meat_poultry", "М'ясо та птиця", [
            Category("pork_beef", "Свинина та яловичина"),
            Category("poultry", "Птиця (курка, індичка)"),
            Category("salo", "Сало та копченості"),
            Category("sausages", "Ковбасні вироби"),
        ]),
        Category("dairy", "Молочна продукція", [
            Category("milk_sour_cream", "Молоко та сметана"),
            Category("cottage_cheese", "Сир домашній / Творог"),
            Category("hard_cheese", "Тверді сири та бринза"),
            Category("butter", "Масло"),
        ]),
        Category("fish_seafood", "Риба та морепродукти", [
            Category("fresh_fish", "Свіжа та жива риба"),
            Category("frozen_fish", "Морожена риба"),
            Category("smoked_fish", "Копчена та в'ялена риба"),
        ]),
        Category("grocery_sweets", "Бакалія, спеції та солодощі", [
            Category("spices", "Спеції та приправи"),
            Category("honey_nuts", "Мед, горіхи та сухофрукти"),
            Category("sweets", "Солодощі та печиво"),
            Category("tea_coffee", "Чай та кава"),
            Category("grains_pasta", "Крупи, макарони, олія"),
        ]),
        Category("bakery", "Хліб та випічка", [
            Category("fresh_bread", "Свіжий хліб"),
            Category("pastries", "Пиріжки та булочки"),
            Category("lavash", "Лаваші та коржі"),
        ]),
    ]),
    Category("clothing_footwear", "👗 Одяг, взуття та аксесуари", [
        Category("mens_clothing", "Чоловічий одяг", [
            Category("mens_outerwear", "Верхній одяг"),
            Category("mens_casual", "Повсякденний одяг"),
            Category("mens_sportswear", "Спортивний одяг"),
            Category("mens_underwear", "Білизна та шкарпетки"),
        ]),
        Category("womens_clothing", "Жіночий одяг", [
            Category("womens_outerwear", "Верхній одяг"),
            Category("womens_dresses", "Сукні, спідниці, блузи"),
            Category("womens_casual", "Штани, джинси, кофти"),
            Category("womens_underwear", "Білизна та колготи"),
        ]),
        Category("kids_clothing", "Дитячий одяг", [
            Category("baby_clothing", "Одяг для немовлят"),
            Category("kids_outerwear", "Дитячий верхній одяг"),
            Category("school_uniform", "Шкільна форма та святковий одяг"),
        ]),
        Category("footwear", "Взуття", [
            Category("mens_shoes", "Чоловіче взуття"),
            Category("womens_shoes", "Жіноче взуття"),
            Category("kids_shoes", "Дитяче взуття"),
            Category("home_shoes", "Капці та гумове взуття"),
        ]),
        Category("accessories_bags", "Сумки та аксесуари", [
            Category("bags_backpacks", "Сумки, рюкзаки, валізи"),
            Category("wallets_belts", "Гаманці та ремені"),
            Category("hats_scarves", "Шапки, кепки, шарфи"),
            Category("umbrellas", "Парасолі"),
        ]),
    ]),
    Category("home_household", "🏡 Дім, посуд та побут", [
        Category("household_chemicals", "Побутова хімія та гігієна", [
            Category("cleaning_detergents", "Пральні порошки та миючі засоби"),
            Category("personal_care", "Косметика та догляд за тілом"),
            Category("paper_products", "Серветки та туалетний папір"),
        ]),
        Category("kitchen_tableware", "Посуд та кухонне приладдя", [
            Category("pots_pans", "Каструлі та сковорідки"),
            Category("plates_cutlery", "Тарілки, чашки, столові прибори"),
            Category("canning_supplies", "Банки, кришки, закочувальні ключі"),
        ]),
        Category("home_textiles", "Домашній текстиль", [
            Category("bedding", "Постільна білизна"),
            Category("blankets_pillows", "Ковдри та подушки"),
            Category("towels_curtains", "Рушники, штори, скатертини"),
        ]),
        Category("garden_plants", "Сад та город", [
            Category("seeds_seedlings", "Насіння, саджанці, розсада"),
            Category("fertilizers_pest_control", "Добрива та захист рослин"),
            Category("garden_tools", "Садовий інвентар та полив"),
        ]),
    ]),
    Category("tools_hardware", "🛠️ Інструменти та будівництво", [
        Category("hand_power_tools", "Інструменти", [
            Category("hand_tools", "Ручний інструмент"),
            Category("power_tools", "Електроінструмент та розхідники"),
            Category("measuring_tools", "Вимірювальний інструмент"),
        ]),
        Category("hardware_fasteners", "Кріплення та фурнітура", [
            Category("screws_nails", "Саморізи, болти, цвяхи"),
            Category("locks_hinges", "Замки, петлі, ручки"),
        ]),
        Category("plumbing_electrical", "Сантехніка та електрика", [
            Category("plumbing", "Крани, шланги, труби"),
            Category("cables_sockets", "Кабелі, розетки, вимикачі"),
            Category("lighting_bulbs", "Лампи, світильники, ліхтарі"),
        ]),
    ]),
    Category("electronics_gadgets", "📱 Електроніка та аксесуари", [
        Category("phone_accessories", "Мобільні аксесуари", [
            Category("cases_glass", "Чохли та захисне скло"),
            Category("chargers_cables", "Зарядні пристрої та кабелі"),
            Category("headphones_speakers", "Навушники та колонки"),
        ]),
        Category("small_appliances", "Дрібна техніка", [
            Category("kitchen_appliances", "Чайники, блендери, ваги"),
            Category("beauty_appliances", "Фени, машинки для стрижки"),
            Category("batteries_powerbanks", "Батарейки, акумулятори, павербанки"),
        ]),
    ]),
    Category("services", "🔧 Послуги та ремонт", [
        Category("shoe_repair", "Ремонт взуття"),
        Category("clothing_repair", "Ремонт та підшив одягу"),
        Category("phone_repair", "Ремонт телефонів та гаджетів"),
        Category("key_making", "Виготовлення ключів"),
        Category("tool_sharpening", "Заточка ножів та інструменту"),
    ]),
    Category("pet_supplies", "🐾 Товари для тварин", [
        Category("pet_food", "Корми для котів, собак, птахів"),
        Category("pet_accessories", "Повідці, нашийники, миски"),
        Category("veterinary_pharmacy", "Ветпрепарати та захист від бліх"),
    ]),
])


# 1. Build lookup dictionary cleanly in one pass
CATEGORY_MAP: dict[str, Category] = {}


def _index_categories(cat: Category):
    CATEGORY_MAP[cat.id] = cat
    for child in cat.children:
        _index_categories(child)


_index_categories(ROOT_CATEGORY)


def get_category_by_id(cat_id: str) -> Category | None:
    return CATEGORY_MAP.get(cat_id)


def resolve_category_path(path_ids: list[str]) -> Category:
    """Navigates to the current category using the path history."""
    if not path_ids:
        return ROOT_CATEGORY

    return CATEGORY_MAP.get(path_ids[-1], ROOT_CATEGORY)