from django_filters import rest_framework as filters


from people.models import Name, Car, City

class NameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains', label='Есімі')
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='contains', label='Ата-тегі')
    cars = filters.CharFilter(field_name='cars', lookup_expr='exact', label='Көлік')
    city = filters.CharFilter(field_name='city', lookup_expr='exact', label='Қала')


    class Meta:
        model = Name
        fields = ('name', 'first_name', 'cars', 'city')


class CarFilter(filters.FilterSet):
    model = filters.CharFilter(field_name='model', lookup_expr='contains', label='Марка')
    number = filters.NumberFilter(field_name='number', lookup_expr='exact', label='Нөмір')


    class Meta:
        model = Car
        fields = ('model', 'number')


class CityFilter(filters.FilterSet):
    city = filters.CharFilter(field_name="city", lookup_expr='contains', label='Қала')
    author = filters.CharFilter(field_name='author', lookup_expr='exact', label='Иесі')


    class Meta:
        model = City
        fields = ('city', 'author')