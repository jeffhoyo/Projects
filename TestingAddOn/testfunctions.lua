FrostTracker = {}
FT_db = FT_db or {}

-- Sample Event Variables --
local FT = FrostTracker
local event = "CURRENCY_DISPLAY_UPDATE"
local unitName = "Vanthuss"
local arg1 = 341
local arg2 = 70
local count
local FT_db = {
	["Rinestiri"] = {
		["frostTotal"] = 43,
	},
	["Feriosa"] = {
		["frostTotal"] = 0,
	},
	["Vanthuss"] = {
		["frostTotal"] = 96,
	},
}

function FT.UpdateTotal(unitName, weeklyTotal)
    if FT_db[unitName] == nil then
        FT_db[unitName] = {}
    end

    FT_db[unitName].weeklyTotal = weeklyTotal

end

if event == "CURRENCY_DISPLAY_UPDATE" and arg2 ~= 0 then
    -- Fill global variables
    --unitName = UnitName("player")
    local diff;
    local weeklyTotal = 24;
    local nextReset = 1702393200;  --Tuesday, December 12th, 
    local epochWeek = 604800;
    
    --local currentTime = date()
    local currentTime = os.time()
    local currentTotal = FT_db[unitName].frostTotal;
    if currentTime < nextReset then
        if arg2 > currentTotal then
            diff = arg2 - currentTotal;
            weeklyTotal = weeklyTotal + diff;
        end
    end
    --print(arg2)
    --print(unitName.." : "..count)
    print(os.date("%Y-%m-%d_%H:%M:%S", nextReset))
    print(os.date("%Y-%m-%d_%H:%M:%S", currentTime))
    FT.UpdateTotal(unitName, weeklyTotal)
end

print(FT_db[unitName].weeklyTotal)

-- -- Testing reset Generation by Epoch
-- local nextReset = 1702393200;  --Tuesday, December 12th, 
-- local epochWeek = 604800;
-- local i = 1
-- while i < 10 do
--     local nextReset = nextReset + (epochWeek * i)
--     print(os.date("%Y-%m-%d_%H:%M:%S", nextReset))
--     --print(nextReset)
--     i = i + 1
-- end