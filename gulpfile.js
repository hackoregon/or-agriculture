var gulp = require('gulp');
var sass = require('gulp-sass');
var notify = require('gulp-notify');

gulp.task('compileSass', function() {
	gulp.src('./app/assets/scss/*.scss')
	.pipe(sass()
	.on('error', function(err) {
		notify().write(err);
		this.emit('end');
	}))
	.pipe(gulp.dest('./app/assets/css'))
	.pipe(notify('It worked!'));
});

gulp.task('watch', function() {
	gulp.watch('./app/assets/scss/**/*.scss', ['compileSass']);
});

gulp.task('build', ['compileSass']);
