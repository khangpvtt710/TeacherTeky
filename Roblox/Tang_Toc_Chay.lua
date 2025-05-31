--- chọn StarterPlayer -> chọn StarterCharacterScripts 
--- Tạo localScript rồi đổi tên tùy ý

local MaxSpeed = 50 --- tốc độ tối đa
while true do
	wait()
	if script.Parent.Humanoid.MoveDirection == Vector3.new(0,0,0) then
		script.Parent.Humanoid.WalkSpeed = 20
	else
		script.Parent.Humanoid.WalkSpeed = script.Parent.Humanoid.WalkSpeed + 0.5
		if script.Parent.Humanoid.WalkSpeed >= MaxSpeed then
			script.Parent.Humanoid.WalkSpeed = MaxSpeed
		end
	end
 end