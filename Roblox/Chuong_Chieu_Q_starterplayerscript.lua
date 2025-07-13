--- vào starterplayer vào starterplayerscript tạo localscript đặt tên là Fire, thêm vào Fire -> remoteEvent
--lấy thông tin người chơi nhập vào từ bàn phím và chuột
local UserInputService = game:GetService("UserInputService")
--dịch vụ lưu trữ
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local EventFire = ReplicatedStorage:FindFirstChild("Fire")

local Players = game.Players
local player = Players.LocalPlayer
local aiming = false
local mouse = player:GetMouse()

UserInputService.InputBegan:Connect(function(input)
	--kiểm tra người chơi có đang ấn chuột phải hay không ?
	if input.UserInputType == Enum.UserInputType.MouseButton2 then
		aiming = true
	elseif input.KeyCode == Enum.KeyCode.Q then
	--elseif input.UserInputType == Enum.UserInputType.MouseButton1 then
		
		if aiming == true then
			local direction = (mouse.Hit.Position - player.Character:FindFirstChild("Head").Position).Unit
			
			EventFire:FireServer(direction)
		end
		
	end
	
end)


UserInputService.InputEnded:Connect(function(input)
	--kiểm tra người chơi có đang ấn chuột phải hay không ?
	if input.UserInputType == Enum.UserInputType.MouseButton2 then
		aiming = false		
	end

end)





--UserInputService.InputBegan:Connect(function(input)
--	if input.UserInputType == Enum.UserInputType.MouseButton2 then
--		aiming = true
--	elseif input.UserInputType == Enum.UserInputType.MouseButton1 then
--		if aiming then
--			local direction = (mouse.Hit.Position - player.Character:FindFirstChild("Head").Position).unit
--			EventFire:FireServer(direction)
--		end
--	end
--end)