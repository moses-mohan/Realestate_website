from django.db import migrations


PROPERTIES = [
    ('Beach side villa', 'Vishakapatnam', 10000000, "A spacious three bedroom villa with a modern kitchen, a private garden, and parking for two cars. Close to schools, shops, and the main road. Visit us today and step into the home you've always imagined", 'properties/Beach_side__villa.jpg'),
    ("SUN BUILDING'S", 'Vishakapatnam', 10000000, 'IT IS a  Beach 🏖 Side View Villa\nSunny 3 Bedroom Villa in Visakhapatnam: "A spacious villa with a modern kitchen, private garden, and parking for two cars. A bright two bedroom flat with a sea view balcony, just five minutes from the beach.  Visit us today and step into the home you\'ve always imagined', 'properties/cherai-sea-view-villa.jpg'),
    ("Moon Villa's", 'Vishakapatnam', 88888888, 'It has the worlds best night view\nA peaceful four bedroom home near schools and shops, with a large living room and a terrace.  Visit us today and step into the home you\'ve always imagined', 'properties/Glass-House-43-scaled.jpg'),
    ("MJ villa's", 'Vishakapatnam', 19876543, 'MJ Villas builds beautiful, affordable homes for families in Visakhapatnam. From cozy apartments to spacious luxury villas, every home is designed for comfort and style. We handle everything, from choosing your dream home to the final paperwork. Visit us today and step into the home you\'ve always imagine', 'properties/517409512.jpg'),
    ('Palm Grove Villa', 'Vishakapatnam', 12345678, 'A luxury four bedroom villa surrounded by palm trees. It has a private swimming pool and a large garden. The kitchen is modern and fully fitted. Perfect for families who love peace and space.', 'properties/001.jpg'),
    ('Skyline Heights Apartment', 'Vishakapatnam', 124134123413245, 'A stylish three bedroom apartment on the tenth floor. Enjoy a wide city view from the balcony. The building has a gym, lift, and covered parking. Close to the highway and shopping malls.', 'properties/002.avif'),
    ('Lakeview Residency', 'Vishakapatnam', 3212355667, "A calm two bedroom home beside a quiet lake. Large windows let in plenty of natural light. There is a children's play area and a walking path nearby. Ideal for small families and first-time buyers.", 'properties/003.jpg'),
    ('Royal Orchid Mansion', 'Visakhapatnam', 987654321, 'A grand five bedroom mansion with high ceilings and a marble floor. It includes a home theatre, a terrace garden, and servant quarters. The gated compound has round-the-clock security. Built for those who want a true luxury home.', 'properties/004.jpg'),
    ('Sea Breeze Cottage', 'Visakhapatnam', 123456789, 'A cozy three bedroom cottage just a short walk from the beach. The wide front porch is perfect for evening tea. It has a small garden and a fully fitted kitchen. Ideal for a peaceful family life by the sea.', 'properties/005.jpg'),
    ('Emerald Hills Villa', 'Visakhapatnam', 987654321, 'A modern four bedroom villa on a green hillside. Large glass windows give a stunning view of the valley. It includes a private terrace, covered parking, and a home office room. Perfect for those who want calm without leaving the city.', 'properties/006.jpg'),
]


def seed_properties(apps, schema_editor):
    Property = apps.get_model('listings', 'Property')
    for title, city, price, description, image in PROPERTIES:
        Property.objects.get_or_create(
            title=title,
            defaults={
                'city': city,
                'price': price,
                'description': description,
                'image': image,
            },
        )


class Migration(migrations.Migration):
    dependencies = [('listings', '0003_inquiry')]

    operations = [migrations.RunPython(seed_properties, migrations.RunPython.noop)]
