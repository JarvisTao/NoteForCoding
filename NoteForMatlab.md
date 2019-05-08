## Notes for Matlab coding

1. **Str** operation functions.

   * find **pattern** in specific **string**.

     ```matlab
     str = 'I love coding.';
     loc = strfind(str, 'love'); % return '3'
     str(1:loc-1); % returen 'I '
     ```

   * and so on

2. **File** operation functions

   * Find specific ***Pattern*** file in specific file folder.

   * ```matlab
     infolder = '/your/working/folder';
     files = dir([infolder,'*pattern_here*.tif']);% contain: name, folder, date...
     ```

   * and  so on

3. **WaitBar** functions

   ```matlab
   h = waitbar(0,'please wait');
   for i = 1:1000
   	str = ['Running... ',num2str(i/1000*100),'%'];
   	waitbar(i/1000,h,str)
   end
   ```

4. **Save** variables or workflow to specific files.(***.mat or *.txt**)

   ```matlab
   save('filename', 'var1', 'var2', ...)：%保存指定的变量在 filename 指定的文件中。
   save('filename', '-struct', 's')：%保存结构体s中全部域作为单独的变量。
   save('filename', '-struct', 's', 'f1', 'f2', ...)：%保存结构体s中的指定变量。
   save('-regexp', expr1, expr2, ...)：%通过正则表达式指定待保存的变量需满足的条件。
   save('..., 'format'); %指定保存文件的格式，格式可以为MAT文件、ASCII文件等
   ```

   