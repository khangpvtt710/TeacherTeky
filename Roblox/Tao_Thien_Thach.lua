-- tạo scripts ở workspace


-- Tạo một thiên thạch từ "ReplicatedStorage" hoặc "ServerStorage"
local replicatedStorage = game:GetService("ReplicatedStorage")
local players = game:GetService("Players")
local debris = game:GetService("Debris")

-- Tạo một hàm để tạo thiên thạch
local function createMeteor()
	-- Tạo Part cho thiên thạch
	local meteor = Instance.new("Part")
	meteor.Shape = Enum.PartType.Ball
	meteor.Size = Vector3.new(5, 5, 5)
	meteor.Anchored = false
	meteor.CanCollide = true
	meteor.BrickColor = BrickColor.new("Bright red")
	meteor.Material = Enum.Material.SmoothPlastic
	meteor.Position = Vector3.new(math.random(-500, 500), 200, math.random(-500, 500)) -- Đặt thiên thạch xuất phát từ vị trí ngẫu nhiên trên bầu trời
	meteor.Parent = workspace

	-- Rơi xuống (di chuyển xuống dưới)
	local bodyVelocity = Instance.new("BodyVelocity")
	bodyVelocity.MaxForce = Vector3.new(4000, 4000, 4000)
	bodyVelocity.Velocity = Vector3.new(0, -50, 0)  -- Điều chỉnh tốc độ rơi xuống
	bodyVelocity.Parent = meteor

	-- Debug: In thông báo khi thiên thạch va vào vật thể
	meteor.Touched:Connect(function(hit)
		print("Meteor touched something!") -- In ra khi thiên thạch va chạm với vật thể
		local character = hit.Parent
		local humanoid = character:FindFirstChildOfClass("Humanoid")

		-- Nếu va chạm với nhân vật người chơi và có Humanoid, người chơi sẽ chết
		if humanoid then
			print("Meteor hit a player!")  -- In ra nếu va chạm với người chơi
			humanoid.Health = 0
		end
	end)

	-- Xóa thiên thạch sau khi rơi xuống đất
	debris:AddItem(meteor, 5)
end

-- Tạo hiệu ứng rơi thiên thạch ngẫu nhiên mỗi 3 giây
while true do
	wait(0.1)  -- Thiên thạch sẽ rơi ngẫu nhiên sau khoảng thời gian từ 3 đến 5 giây
	createMeteor()
end
