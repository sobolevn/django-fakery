from django_fakery import factory, shortcuts

chef = factory.blueprint("tests.Chef", fields={"first_name": "Chef {}"})


pizza = factory.blueprint(
    "tests.Pizza",
    fields={
        "chef": chef,
        "thickness": 1,
        "expiration": shortcuts.future_date("+7d"),
        "baked_on": shortcuts.past_datetime("-1h"),
    },
)


chef_short = factory.blueprint("tests.Chef").fields(first_name="Chef {}")

pizza_short = factory.blueprint("tests.Pizza").fields(chef=chef_short, thickness=1)
