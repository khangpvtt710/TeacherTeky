--- chọn StarterPlayer -> chọn StarterCharacterScripts 
--- Tạo localScript rồi đổi tên tùy ý
--- tạo animation rồi đặt tên Run, Jump, Idle
local walkAnimation = script:WaitForChild("Run")
local JumpAnimation = script:WaitForChild("Jump")
local idleAnimation = script:WaitForChild("Idle")
local Char = script.Parent
local Humanoid = Char:WaitForChild("Humanoid")
local animationTrack1 = Humanoid:LoadAnimation(walkAnimation)
local animationTrack2 = Humanoid:LoadAnimation(JumpAnimation)
local animationTrack3 = Humanoid:LoadAnimation(idleAnimation)

Humanoid.Running:Connect(function(movementSpeed)
	if movementSpeed > 0 then
		if not animationTrack1.IsPlaying then
			animationTrack3:Stop()
			animationTrack1:Play()
		end
	else
		if animationTrack1.IsPlaying then
			animationTrack1:Stop()
			animationTrack3:Play()
		end
	end
end)

Humanoid.Jumping:Connect(function()
	animationTrack2:Play()
end)