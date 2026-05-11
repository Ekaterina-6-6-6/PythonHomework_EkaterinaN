from address import Address
from mailing import Mailing


sender_address = Address("400001", "Волгоград", "Козловская", "13", "-")
recipient_address = Address(
    "400124", "Волгоград", "Улица 'Победы'", "50а", "-"
)

mailing = Mailing(
    to_address=recipient_address,
    from_address=sender_address,
    cost=38.00,
    track="Автобуса",
)

print(
    f"Отправление {mailing.track} из"
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house}"
    f" - {mailing.from_address.apartment} "
    f" в {mailing.to_address.index}, {mailing.to_address.city},"
    f" {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}."
    f" Стоимость {mailing.cost} рублей."
)
