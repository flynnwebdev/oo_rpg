class Character
    attr_reader :name, :race

    def initialize(name, race)
        @name = name
        @race = race
    end
end

module Combatable
    def combatable_initialize(hp=50, attack=10)
        @hp = hp
        @attack = attack
    end

    def battle
    end
end

class Warrior < Character
    include Combatable

    def initialize(name, race)
        super(name, race)
        combatable_initialize(80, 20)
    end
end

class Mage < Character
    include Combatable

    def initialize(name, race)
        super(name, race)
        combatable_initialize(40, 30)
    end
end

class Totem
    include Combatable

    def initialize(hp, attack)
        combatable_initialize(hp, attack)
    end
end

class Vendor < Character
    def initialize(name, race)
        super(name, race)
        @goods = []
        @gold = 1000
    end
end

conan = Warrior.new("Conan", "Human")
galadriel = Mage.new("Galadriel", "Elf")
grok = Vendor.new("Grok", "Orc")
fireTotem = Totem.new(10, 20)

p conan
p galadriel
p grok
p fireTotem
