class Reindeer {
    int distance;
    int speed;
    int moveDuration;
    int restDuration;
    boolean isResting = false;
    int time = 0;

    public Reindeer(int speed, int moveDuration, int restDuration) {
        this.distance = 0;
        this.speed = speed;
        this.moveDuration = moveDuration;
        this.restDuration = restDuration;
    }

    public int getDistance(){
        return distance;
    }

    public int getMoveDuration(){
        return moveDuration;
    }

    public int getRestDuration(){
        return restDuration;
    }

    public int getSpeed(){
        return speed;
    }

    public void move(){
        if (!isResting) {
            distance += speed;
            time++;

            if (time >= moveDuration) {
                isResting = !isResting;
                time = 0;
            }
        } else {
            time++;
            if (time >= restDuration) {
                isResting = !isResting;
                time = 0;
            }
        }
    }
}