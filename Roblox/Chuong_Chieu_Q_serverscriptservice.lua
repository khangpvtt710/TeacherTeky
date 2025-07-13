--- tạo localscript trong serverscriptservice đặt tên Fire
--Lấy remote event "Fire" để nhận hướng từ client
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local EventFire = ReplicatedStorage:FindFirstChild("Fire")
local Debris = game:GetService("Debris")

local touchSound = ReplicatedStorage:FindFirstChild("touch"):Clone()
local shootSound = ReplicatedStorage:FindFirstChild("shoot"):Clone()

local bullet = Instance.new("Part")
bullet.Name = "bullet"
bullet.Shape = Enum.PartType.Ball
bullet.Size = Vector3.new(3,3,3)
bullet.Material = Enum.Material.Neon
bullet.CanCollide = false

shootSound.Parent = bullet
--shootSound.Volume = 1
touchSound.Parent = bullet
--touchSound.Volume = 1


EventFire.OnServerEvent:Connect(function(player, message)
	local bullet2 = bullet:Clone()
	
	bullet2.Touched:Connect(function(hit)
		local humanoid = hit.Parent:FindFirstChild("Humanoid")
		
		if humanoid and humanoid.Parent.Name ~= player.Name then
			touchSound:Play()
			humanoid.Health -= 10
			
			if humanoid.Health <= 0 then
				humanoid.Parent:Destroy()
			end
			
		end
		
	end)
	
	bullet2.Parent = workspace
	bullet2.Position = player.Character:FindFirstChild("Head").Position
	
	shootSound:Play()
	
	bullet2.AssemblyLinearVelocity = message * 300
	wait(0.0005)
	bullet2.CanCollide = true

	Debris:AddItem(bullet2, 3)
end)



--local bullet2 = bullet:Clone()
--bullet2.Parent = workspace
--bullet2.Position = player.Character:FindFirstChild("Head").Position
--bullet2.AssemblyLinearVelocity = direction * 300
--wait(0.0005)
--bullet2.CanCollide = true
--Debris:AddItem(bullet2, 5)
