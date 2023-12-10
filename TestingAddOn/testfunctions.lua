FrostTracker = {}
FT_db = FT_db or {}

-- Sample Event Variables --
local FT = FrostTracker
local event = "CURRENCY_DISPLAY_UPDATE"
local unitName = "Vanthuss"
local arg1 = 341
local arg2 = 100
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
    local nextReset = 1702393200;
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
    FT.UpdateTotal(unitName, weeklyTotal)
end
print(FT_db[unitName].weeklyTotal)