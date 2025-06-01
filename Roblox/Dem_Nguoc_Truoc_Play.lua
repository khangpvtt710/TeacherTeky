-- chọn starterGui tạo 1 screenGui, trong screenGui tạo Label sửa text thành 10 và đổi tên thành CountdownLable

-- tạo scripts trong serverscriptservice
local Players = game:GetService("Players")

local WAITING_POSITION = workspace:FindFirstChild("WaitingPosition") -- Vị trí chờ
local START_POSITION = workspace:FindFirstChild("StartPosition") -- Vị trí bắt đầu

local COUNTDOWN_TIME = 10 -- Thời gian đếm ngược

Players.PlayerAdded:Connect(function(player)
	player.CharacterAdded:Connect(function(character)
		-- Dịch chuyển người chơi đến vị trí chờ
		local humanoidRootPart = character:WaitForChild("HumanoidRootPart")
		if WAITING_POSITION then
			humanoidRootPart.CFrame = WAITING_POSITION.CFrame + Vector3.new(0, 3, 0)
		end

		-- Gửi sự kiện UI để hiển thị đếm ngược
		local playerGui = player:FindFirstChild("PlayerGui")
		if playerGui then
			local countdownGui = playerGui:FindFirstChild("ScreenGui")
			if countdownGui then
				local label = countdownGui:FindFirstChild("CountdownLabel")
				if label then
					-- Đếm ngược
					for i = COUNTDOWN_TIME, 0, -1 do
						label.Text = tostring(i)
						wait(1)
					end
					label.Text = "GO!" -- Hiển thị "GO!" trong 1 giây
					wait(1)
					label.Text = "" -- Ẩn UI sau khi đếm ngược kết thúc
				end
			end
		end

		-- Sau khi đếm ngược, dịch chuyển người chơi đến vị trí bắt đầu
		if START_POSITION then
			humanoidRootPart.CFrame = START_POSITION.CFrame + Vector3.new(0, 3, 0)
		end
	end)
end)
