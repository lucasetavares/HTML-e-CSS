local distanceToSpells = 2
local distanceToTarget = 4
local pokeTeam = {"Gamabunta", "Mavi", "White Florges", "Shiny Starmie", "Bonnie", "Shiny Feraligatr"}
local moveSet1 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" , "m10"} -- Pokemon 1
local moveSet2 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" } -- Pokemon 2
local moveSet3 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" , "m10"} -- Pokemon 3
local moveSet4 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" } -- Pokemon 4
local moveSet5 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" } -- Pokemon 5
local moveSet6 = {"m1", "m2", "m3", "m4", "m5", "m6", "m7" , "m8" , "m9" , "m10"} -- Pokemon 6
local toggleCombo = true

local screenCreatures = g_game.getCreatures()
local mainPlayer = g_game.getLocalPlayer()

if #ggame.getMonstersAround(distanceToTarget) >= 1 then
    for , creature in pairs(screenCreatures) do
        creatureType = creature:getType()
        creaturePosition = creature:getPosition()
        if creatureType == 1 and mainPlayer:getPosition():getDistance(creaturePosition) <= distanceToTarget then
            if not g_game.isAttacking() then
        sleep(500)
        g.game_attack(creature)
            end
        end
        if ggame.isAttacking() and toggleCombo == true then
            for.creature in pairs(screenCreatures)do
            creatureType=creature:getType()
            creaturePosition2=creature:getPosition()
            if creatureType == 3 and
        mainPlayer:getPosition():getDistance(creaturePosition2) <= distanceToSpells then
        for pos, name in ipairs(pokeTeam)do
        creatureName = creature:getName()
        if string.find(creatureName, name) then
        if pos == 1 then
            for_ move in pairs(moveSet1)do 
                ggame.talk(move)
            end            
        end 
        if pos == 2 then
            for, move in pairs(moveSet2)do  
                ggame.talk(move)
            end
            if pos == 3 then
                for, move in pairs(moveSet3)do
                    ggame.talk(move)
                end
            end
            if pos == 4 then
                for, move in pairs(moveSet4)do
                    ggame.talk(move)
                end
            end
            if pos == 5 then
                for, move in pairs(moveSet5)do
                    ggame.talk(move)
                end
            end
            if pos == 6 then
                for, move in pairs(moveSet6)do
                    ggame.talk(move)
            end
        end
    end
end
auto(100)