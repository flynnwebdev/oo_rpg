class Address
    attr_reader :street, :city, :postcode

    def initialize(street, city, postcode)
        @street = street
        @city = city
        @postcode = postcode
    end

    def to_s
        return "#{@street}, #{@city}, #{@postcode}"
    end
end

class Person
    attr_reader :address

    def initialize(name, age, street, city, postcode)
        @name = name
        @age = age
        # Person "has-a" Address
        @address = Address.new(street, city, postcode)
        # @address = { street: street, city: city, postcode: postcode }
    end

    def to_s
        return "#{@name} is #{@age} years old, and lives at #{@address}"
    end

    # def full_address
    #     return @address.full
    # end
end


# addr = Address.new("12 Any Street", "Brisbane", 4000)
matt = Person.new("Matt", 49, "12 Any Street", "Brisbane", 4000)
# p matt
puts matt


