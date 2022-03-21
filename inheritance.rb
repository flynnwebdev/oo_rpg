class Animal
    attr_accessor :name

    def initialize(name)
        @name = name
    end

    def speak
        return "Hello!"
    end
end

# Dog "is-a" Animal
class Dog < Animal
    attr_reader :breed

    def initialize(name, breed)
        super(name)
        @breed = breed
    end

    def speak
        return "#{super} Woof! I am a #{breed}"
    end
end

class Cat < Animal
end

# Main
fido = Dog.new("Fido", "Border Collie")
felix = Cat.new("Felix")
puts fido.speak
puts felix.speak
# p fido
# p felix