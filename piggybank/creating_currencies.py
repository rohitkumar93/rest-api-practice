
# python code to manually add some currencies
# run this in django shell
from piggybank.models import Currency


Currency.objects.bulk_create([Currency(code="USD", name="United States Dollar"), Currency(code="GBP", name="Great Britain Pound"), Currency(
    code="EUR", name="European Union Euro"), Currency(code="INR", name="Indian Rupee"), Currency(code="JPY", name="Japanese Yen"), Currency(code="RUN", name="Russia Ruble")])
