% NXT Robot No : PC 02

COM_CloseNXT('all');
close all;
h = COM_OpenNXT();
COM_SetDefaultNXT(h);
mA = NXTMotor('A');
mA.Power = -10;
mB = NXTMotor('B');
mB.Power = -10;
mAB = NXTMotor('AB', 'Power', 40); % creates an object for AC motors
% mAC.SendToNXT();
OpenLight (SENSOR_2,'ACTIVE');
OpenLight (SENSOR_3,'ACTIVE');
%mA.SendToNXT();
%mC.SendToNXT();
%SwitchLamp(Motor_A, 'on');
white_val_1 = 650;
white_val_2 = 600;

black_val_1 = 450;
black_val_2 = 400;

green_val_1_min = 445;
green_val_1_max = 515;
green_val_2_min = 400;
green_val_2_max = 490;

gray_val_1_min = 515;
gray_val_1_max = 620;
gray_val_2_min = 491;
gray_val_2_max = 610;

purple_val_1_min = 560;
purple_val_1_max = 585;
purple_val_2_min = 500;
purple_val_2_max = 520;

SwitchLamp(MOTOR_C, 'off');
OpenUltrasonic(SENSOR_1);

% White : go forward
% white color = 740 (sensor 2) NEW : 671, 748, 754
% white color = 693 (sensor 3) NEW : 607, 703, 679

% black color = 437 (sensor 2) NEW : 432, 434, 428
% black color = 382 (sensor 3) NEW : 373, 471, 390

% green color = 462 (sensor 2) NEW : 503, 485, 451, 493, 498, 494, 512
% green color = 418 (sensor 3) NEW : 450, 441, 407, 435, 434, 438, 484

%gray color = 593 (sensor 2) NEW : 596, 600, 581, 579, 593, 597, 532, 600
%gray color = 531 (sensor 3) NEW : 547, 538, 521, 522, 529, 529, 459, 526

%purple color = 572 (sensor 2) NEW : 575, 610, 610, 609
%purple color = 515 (sensor 3) NEW : 621, 543, 544, 540 
loop = true;
atend = 0;
foundgray = 0;
slowzone = 0;
while(loop)
    light_1 = GetLight(SENSOR_2);
    light_2 = GetLight(SENSOR_3);
    %mAC.SendToNXT();
    %disp(light_1);
    %disp(light_2);
    val = GetUltrasonic(SENSOR_1);
    if(val < 10)
        mAB.Stop('off');
    
    elseif(light_1 < black_val_1 && light_2 > black_val_2)
        % Black : turn right
%         disp('Black - turn right zone');
%         disp(light_1);
%         disp(light_2);
        mAB.Stop('off');
        Turnright(mA);
    elseif(light_1 > black_val_1 && light_2 < black_val_2)
        % Black : turn left
%         disp('Black - turn left zone');
%         disp(light_1);
%         disp(light_2);
        mAB.Stop('off');
        Turnleft(mB);
    elseif(light_1 > white_val_1 && light_2 > white_val_2) % white zone
        % light off
        % normal speed
        %disp('White zone');
        %disp(light_1);
        %disp(light_2);
        SwitchLamp(MOTOR_C, 'off');
        if(foundgray == 1)
            % Enter white after 1st gray
            foundgray = 2;
        end
        if(foundgray == 3)
            free = Checkparking(h, mA, mB, mAB);
            
            if(free == 0)
                loop = false;
                disp('No free parking - stops loop');
            else 
                Moveforward(mAB);
            end
            mAB.Power = 25;
            foundgray = 4;
            atend = 1;
        else
            Moveforward(mAB);
        end
    elseif((light_1 >  gray_val_1_min && light_1 < gray_val_1_max) && (light_2 > gray_val_2_min && light_2 < gray_val_2_max)) %Check interval for sensor for the colors
        %Gray zone
        % slow speed
        % light on
        if(atend == 1 && foundgray == 4)
            disp('Gray - at end zone');
            disp(light_1);
            disp(light_2);
            SwitchLamp(MOTOR_C, 'off');
            mAB.Stop('off');
            loop = false;
            %zdisp('if 1');
        elseif(foundgray < 2)
            disp('Gray - slow zone');
            %disp(light_1);
            %disp(light_2);
            SwitchLamp(MOTOR_C, 'on');
            Goslow(mAB);
            slowzone = slowzone + 1;
            if (slowzone > 5)
                foundgray = 1;
            end
            %disp('if 3');
        elseif(foundgray == 2)
            disp('Gray - purple zone');
            mA.Power = -5;
            mB.Power = -5;
            disp(light_1);
            disp(light_2);
            SwitchLamp(MOTOR_C, 'off');
            Moveforward(mAB);
            foundgray = 3;
        else
           disp('gray no zone');
           Moveforward(mAB);
            
        end
    elseif((light_1 >  green_val_1_min && light_1 < green_val_1_max) && (light_2 > green_val_2_min && light_2 < green_val_2_max)) %Check interval for sensor for the colors
        %Green zone
        % high speed
        % light off
        %SwitchLamp(Motor_C, 'on');
        disp('Green zone');
        disp(light_1);
        disp(light_2);
        SwitchLamp(MOTOR_C, 'off');
        Highspeed(mAB);
        % Values needed to be checked : Red, Green, Gray
        
    else
        %disp('cant enter any cases');
        %mAB.Stop('off');
        %pause(0.5);
        Moveforward(mAB);
        %Goslow(mAB);
        %disp(light_1);
        %disp(light_2);
        
    end
    % sensor 2 = right light
    % sensor 3 = left light
end
disp('turning off');
OpenLight (SENSOR_2,'INACTIVE');
OpenLight (SENSOR_3,'INACTIVE');
mAB.Stop('off');
COM_CloseNXT('all');
close all;