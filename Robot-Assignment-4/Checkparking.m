function [ free ] = Checkparking(h, A, B, AB )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    COM_SetDefaultNXT(h);
    AB.Stop('off');
    A.Power = -10;
    B.Power = -10;
    free = 0;
    time = 0.7;
    while(free == 0)
        disp('Check for parking');
        pause(2);
        A.SendToNXT();
        pause(time);
        A.Stop('off');
        pause(1);
        val = GetUltrasonic(SENSOR_1);
        disp(val);
        if(val < 35)
            disp('Right parking is not free');
            B.SendToNXT();
            pause(1.4);
            B.Stop('off');
            pause(0.5);
            val = GetUltrasonic(SENSOR_1);
            disp(val);
            if(val < 35)
                disp('Left parking is not free');
                AB.SendToNXT();
                pause(0.7);
                AB.Stop('off');
                time = 1.4;
            else
                free = 1;
            end
        else
            free = 1;
        end
    end
    disp('found parking');
    AB.Power = 25;
    AB.SendToNXT(); 
    pause(1.2);
    free = 1;
    return;
end

