class SimplePIDController:
    """A simplified PID Controller for rocket stabilization."""
    
    def __init__(self, kp, ki, kd):
        """Initialize the PID controller with gain values."""
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        
        self.prev_error = None
        self.integral = 0
    
    def update(self, target, current, dt):
        """Calculate control output based on target and current values.
        
        Args:
            target: Target value (desired angle, e.g., 0 for vertical)
            current: Current value (current angle)
            dt: Time step
            
        Returns:
            Control output (torque/force to apply)
        """
        error = target - current
        
        if self.prev_error is None:
            self.prev_error = error

        p_term = self.kp * error
        
        self.integral += error * dt
        i_term = self.ki * self.integral
        
        derivative = (error - self.prev_error) / dt
        d_term = self.kd * derivative
        
        self.prev_error = error
        
        return p_term, i_term, d_term
