FrostTracker = {}
FT_db = FT_db or {} -- Shared Variable

local unitName, nextReset, arg2, currencyId
local FT = FrostTracker

local FrostTracker_Frame = CreateFrame("Frame")
--FrostTracker_Frame:RegisterEvent("CURRENCY_DISPLAY_UPDATE")
FrostTracker_Frame:RegisterEvent("PLAYER_ENTERING_WORLD")

function FT.UpdateTable(unitName, currencyAmount)
    if FT_db[unitName] == nil then
        FT_db[unitName] = {}
    end

    FT_db[unitName].frostTotal = currencyAmount

end

function FT.UpdateTotal(unitName, weeklyTotal)
    if FT_db[unitName] == nil then
        FT_db[unitName] = {}
    end

    FT_db[unitName].runningTotal = weeklyTotal

end

function FT.GetData()
    local info = C_CurrencyInfo.GetCurrencyInfo(341);
    currencyAmount = info.quantity
    FT.UpdateTable(unitName, currencyAmount)

end

function FT.OnEvent(self, event, arg1, arg2)

    if event == "PLAYER_ENTERING_WORLD" then
        -- Fill global variables
		unitName = UnitName("player")
        FT.GetData()
	end

    if event == "CURRENCY_DISPLAY_UPDATE" and arg2 ~= 0 then
        -- Fill global variables
        unitName = UnitName("player")
        local diff
        local weeklyTotal = 24
        local nextReset = 1702393200;
        local epochWeek = 604800;
        local currentTime = date()
        local currentTotal = FT_db[unitName].frostTotal;
        if currentTime < nextReset then
            if arg2 > currentTotal then
                diff = arg2 - currentTotal;
                weeklyTotal = weeklyTotal + diff;
            end
        end
        FT.UpdateTotal(unitname, weeklyTotal)
	end
end

FrostTracker_Frame:SetScript("OnEvent", FT.OnEvent)