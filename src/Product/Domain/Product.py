class Product:
    def __init__(self, id: int, name: str, price: float, stock: int, brand: str, category: str, description: str, image: []):
        self._id = id
        self.title = name
        self.description = description
        self.price = price
        self.stock = stock
        self.brand = brand
        self.category = category
        self.image = image

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title 
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def stock(self) -> int:
        return self._stock
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @property
    def category(self) -> str:
        return self._category
    
    @property
    def image(self) -> []:
        return self._image
    