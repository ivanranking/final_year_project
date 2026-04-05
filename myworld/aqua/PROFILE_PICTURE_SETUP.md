# Profile Picture Feature Configuration

## Overview
The AquaSentinel application has been configured to support profile pictures for users. Users can now upload profile pictures that are displayed on the team page and in their user profile.

## What Was Changed

### 1. **Models** (`aquasentinel/models.py`)
- Added `UserProfile` model that extends Django User model with:
  - `bio`: Text field for user biography
  - `role`: Character field for user role (e.g., Developer, Manager)
  - `profile_picture`: ImageField for storing uploaded profile pictures

### 2. **Forms** (`aquasentinel/forms.py`)
- Added `UserProfileForm` to handle profile picture uploads and additional user information
- Form includes validation for images and stylized form controls

### 3. **Views** (`aquasentinel/views.py`)
- Updated `settings()` view to:
  - Automatically create UserProfile for users
  - Handle both user form and profile form submissions
  - Support multipart form data for file uploads

### 4. **Admin Panel** (`aquasentinel/admin.py`)
- Registered `UserProfileAdmin` to manage user profiles from Django admin
- Display user role, name, and upload timestamps

### 5. **Templates** (`aquasentinel/templates/`)
- **team.html**: Updated to display profile pictures instead of avatars
  - Shows uploaded profile picture if available
  - Falls back to icon if no picture uploaded
- **settings.html**: Enhanced with profile picture upload form
  - Displays current profile picture
  - File input for uploading new pictures
  - Sections for bio and role information

### 6. **Static Configuration**
- **settings.py**: 
  - Added `MEDIA_URL = 'media/'`
  - Added `MEDIA_ROOT = BASE_DIR / 'media'`
- **urls.py**: 
  - Added media file serving in development mode
- **style.css**: 
  - Added `.member-avatar` styling for circular profile pictures
  - Added `.profile-upload-section` styling for upload form
  - Added `.profile-img` styling for profile images

### 7. **Signals** (`aquasentinel/signals.py`)
- Auto-creates UserProfile when a new user is created
- Ensures profile exists for every user

### 8. **Migrations** (`aquasentinel/migrations/0002_userprofile.py`)
- Creates UserProfile table with all necessary fields

## How to Use

### For Users:
1. Navigate to **Settings** page (user profile menu)
2. Scroll to **Profile Picture** section
3. Click "Upload New Profile Picture" to select an image file
4. Fill in additional information like Role and Bio (optional)
5. Click "Save changes"
6. Profile picture will appear on the team page and in user profile

### For Administrators:
1. Go to Django Admin panel (`/admin/`)
2. Navigate to **User Profiles**
3. Select a user to manage their profile
4. Upload or change profile picture, role, and bio
5. Save changes

### Profile Picture Requirements:
- **Format**: JPG, PNG, GIF, WebP, or other standard image formats
- **Location**: Stored in `media/profile_pictures/` directory
- **Display**: Circular format with 150x150px on team page

## Setting Up Locally

After pulling these changes:

1. **Install required package** (if not already installed):
   ```bash
   pip install Pillow
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create media directory** (if it doesn't exist):
   ```bash
   mkdir media
   mkdir media/profile_pictures
   ```

4. **Add profile pictures**:
   - Place image files in `media/profile_pictures/` or upload through the settings form
   - Supported formats: JPEG, PNG, GIF, WebP

5. **Test locally**:
   - Start the development server: `python manage.py runserver`
   - Go to Settings page to upload a profile picture
   - Visit the team page to see your profile picture displayed

## Features

✅ Automatic UserProfile creation when new users register
✅ Upload profile pictures through settings form
✅ Display profile pictures on team page with fallback to icon
✅ Admin panel for managing user profiles
✅ Role and bio fields for user information
✅ Responsive image styling
✅ Secure file upload with Django built-in validation

## File Structure
```
media/
  profile_pictures/
    username_profile.jpg
    another_user_profile.png
    ...
```

## Notes
- Profile pictures are served from the `media/` directory in development
- In production, you should use a CDN or S3 for file storage
- Existing users won't have a profile picture until they upload one
- The team page gracefully falls back to the user icon if no picture exists
