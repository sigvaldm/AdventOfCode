! Compile and run with
!   $ gfortran a.f90; ./a.out

module stuff
    type tPath
        integer :: points(32,2)
        integer :: num_points = 0
    end type

contains

    subroutine draw(map, x_min, x_max, y_min, y_max)
        logical, intent(in) :: map(:,:)
        integer, intent(in) :: x_min, x_max, y_min, y_max

        integer :: i, j
        do j=1, y_max-y_min+1
            do i=1, x_max-x_min+1
                if(map(i,j) .eqv. .true.) then
                    write(*,'(A)',advance="no") "#"
                else
                    write(*,'(A)',advance="no") "."
                end if
            end do
            write(*,'(A)') ""
        end do
    end subroutine

end module

program a
    use stuff
    implicit none

    integer :: i, j, k, num_grains
    integer :: x_min, x_max, y_min, y_max
    integer :: file, ierr, idx, comma, dx, dy, dash
    character(len=1000) :: line
    logical, allocatable :: map(:,:)
    logical :: landed
    integer :: x0, x1, y0, y1
    integer :: grain(2), next_grain(2), delta_grain(3,2)

    type(tPath) :: paths(1000)
    type(tPath) :: path
    integer :: num_paths = 0
    integer :: num_points = 0

    ! READ FILE

    open(newunit=file, file='input.txt')
    do
        read(file, '(A)', iostat=ierr) line 
        if(ierr/=0) exit

        num_paths = num_paths + 1
        num_points = 0

        do
            num_points = num_points + 1

            comma = scan(line, ",")
            dash = scan(line, "-")

            read(line(1:comma-1), *) dx
            if(dash==0) then
                read(line(comma+1:), *) dy
            else
                read(line(comma+1:dash-1), *) dy
                line = line(dash+2:)
            end if

            paths(num_paths) % points(num_points,1) = dx
            paths(num_paths) % points(num_points,2) = dy
            paths(num_paths) % num_points = num_points
            ! print *, dx, dy
            if(dash==0) exit
        end do
    end do

    ! FIND DIMENSIONS OF MAP

    x_max = 0
    x_min = 1000
    y_max = 0
    y_min = 0
    do i=1, num_paths
        path = paths(i) 
        do j=1, path % num_points
            if(path % points(j,1) > x_max) x_max = path % points(j,1)
            if(path % points(j,1) < x_min) x_min = path % points(j,1)
            if(path % points(j,2) > y_max) y_max = path % points(j,2)
            if(path % points(j,2) < y_min) y_min = path % points(j,2)
        end do
    end do
    ! print *, x_min, x_max, y_min, y_max

    ! CREATE INITIAL MAP

    allocate(map(x_min:x_max,y_min:y_max))
    map(:,:) = .FALSE.

    do i=1, num_paths
        path = paths(i)
        do j=1, (path % num_points - 1)
            x0 = min(path%points(j,1), path%points(j+1,1))
            x1 = max(path%points(j,1), path%points(j+1,1))
            y0 = min(path%points(j,2), path%points(j+1,2))
            y1 = max(path%points(j,2), path%points(j+1,2))
            map(x0:x1, y0:y1) = .TRUE.
        end do
    end do
    call draw(map, x_min, x_max, y_min, y_max)

    ! POUR SAND

    delta_grain(:,1) = [0, -1, 1]
    delta_grain(:,2) = 1
    num_grains = 0

    grain_loop: do
        grain = [500, 0]
        ! print *, "New grain"
        landed = .FALSE.
        position_loop: do
            direction_loop: do k=1,3
                next_grain = grain + delta_grain(k,:)
                ! print *, next_grain
                if(next_grain(2)>y_max .or. next_grain(1)<x_min .or. next_grain(1)>x_max) then
                    ! Grain leaves the domain. Terminate program.
                    ! print *, "Grain leaves"
                    exit grain_loop
                elseif(map(next_grain(1), next_grain(2))) then
                    ! Space is occupied. Try another direction.
                    ! print *, "Space occupied"
                    if(k==3) exit position_loop
                else
                    ! Space not occupied. Move grain.
                    ! print *, "Space not occupied"
                    grain = next_grain
                    exit direction_loop
                end if
            end do direction_loop
        end do position_loop
        ! print *, "All directions tried"
        ! All directions tried. Place grain and start on new grain.
        map(grain(1), grain(2)) = .TRUE.
        num_grains = num_grains + 1
    end do grain_loop
    call draw(map, x_min, x_max, y_min, y_max)

    print *, num_grains

end program
