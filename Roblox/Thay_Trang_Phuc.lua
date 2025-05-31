local part = script.Parent

local RS = game:GetService("ReplicatedStorage")

part.Touched:Connect(function(hit)
	local character = hit.Parent
	if character then
		local humanoid = character:WaitForChild("Humanoid")
		if humanoid then

			local humanoidDescription = humanoid:GetAppliedDescription()

			humanoidDescription.LeftArm = 78700063178741
			humanoidDescription.RightArm = 78545296849972
			humanoidDescription.LeftLeg = 87038985261881
			humanoidDescription.RightLeg = 106553882417776
			humanoidDescription.Torso = 129107540301967
			humanoidDescription.Head = 129526413374265
			humanoidDescription.HairAccessory = 0
			humanoidDescription.HatAccessory = 0

			humanoid:ApplyDescription(humanoidDescription)

		end
	end
end)

--- https://catalog.roblox.com/v1/bundles/495/details (link lấy mã skin)
--- https://www.roblox.com/catalog?Category=17&salesTypeFilter=1 (link trang chọn skin)