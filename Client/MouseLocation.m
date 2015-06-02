#import <AppKit/AppKit.h>

int main (int argc, const char * argv[]) {
    NSPoint mouseLoc = [NSEvent mouseLocation];
    printf("%lu %lu", (unsigned long)mouseLoc.x, ((unsigned long)mouseLoc.y-900) * -1);
    return 0;
}
