

filename = strcat('C:\Users\Pihan\PycharmProjects\djangoLearningProject\static\video\image.jpg');
Irgb = imread(filename);
Igray = rgb2gray(Irgb);
I = im2double(Igray);

        Gx = [-1 1];
        Gy = Gx';
        Ix = conv2(I,Gx,'same');
        Iy = conv2(I,Gy,'same');
%subplot(1,2,1)
%image(Ix,'CDataMapping','scaled')
%colormap('gray')
%title('Image gradient along X-axis')
%subplot(1,2,2)
%image(Iy,'CDataMapping','scaled')
%colormap('gray')
%title('Image gradient along Y-axis')
        edgeFIS = mamfis('Name','edgeDetection');
        edgeFIS = addInput(edgeFIS,[-1 1],'Name','Ix');
        edgeFIS = addInput(edgeFIS,[-1 1],'Name','Iy');
        sx = 0.07;
        sy = 0.07;
        edgeFIS = addMF(edgeFIS,'Ix','gaussmf',[sx 0],'Name','zero');
        edgeFIS = addMF(edgeFIS,'Iy','gaussmf',[sy 0],'Name','zero');
        edgeFIS = addOutput(edgeFIS,[0 1],'Name','Iout');
        wa = 0.9;
        wb = 1;
        wc = 1;
        ba = 0;
        bb = 0;
        bc = 0.7;
        edgeFIS = addMF(edgeFIS,'Iout','trimf',[wa wb wc],'Name','white');
        edgeFIS = addMF(edgeFIS,'Iout','trimf',[ba bb bc],'Name','black');
        %figure
%subplot(2,2,1)
%plotmf(edgeFIS,'input',1)
%title('X-axis gradient')
%subplot(2,2,2)
%plotmf(edgeFIS,'input',2)
%title('Y-axis gradient')
%subplot(2,2,[3 4])
%plotmf(edgeFIS,'output',1)
%title('Output triangular membership function')
        r1 = "If Ix is zero and Iy is zero then Iout is white";
        r2 = "If Ix is not zero or Iy is not zero then Iout is black";
        edgeFIS = addRule(edgeFIS,[r1 r2]);
        edgeFIS.Rules
        Ieval = zeros(size(I));
        for ii = 1:size(I,1)
            Ieval(ii,:) = evalfis(edgeFIS,[(Ix(ii,:));(Iy(ii,:))]');
        end
        myfig = figure;
        image(Ieval,'CDataMapping','scaled')
        colormap('gray')
        set(0,'DefaultFigureVisible','off')
        axis off
        %title('Edge Detected Image')
        writefile = strcat('C:\Users\Pihan\PycharmProjects\djangoLearningProject\static\video\matlab\class\image.jpg');
        saveas(myfig,writefile)
        %exportgraphics(myfig,writefile,'Resolution',250)
        close(myfig)

  

